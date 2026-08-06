from flask import Blueprint, g, redirect, request, url_for, flash, render_template

from blueprints.auth import login_required
from db import get_db

union_bp = Blueprint('union', __name__, url_prefix='/union')


@union_bp.route('/vote', methods=('POST',))
@login_required
def vote():
    stance = request.form.get('stance')

    if stance not in ('for', 'against'):
        flash('Invalid vote.')
        return redirect(request.referrer or url_for('home'))

    db = get_db()
    db.execute(
        'INSERT INTO union_vote (user_id, stance)'
        ' VALUES (?, ?)'
        ' ON CONFLICT(user_id) DO UPDATE SET stance = excluded.stance,'
        ' created = CURRENT_TIMESTAMP',
        (g.user['id'], stance)
    )
    db.commit()

    return redirect(request.referrer or url_for('home'))


@union_bp.app_context_processor
def inject_union_tally():
    db = get_db()

    for_count = db.execute(
        "SELECT COUNT(*) FROM union_vote WHERE stance = 'for'"
    ).fetchone()[0]

    against_count = db.execute(
        "SELECT COUNT(*) FROM union_vote WHERE stance = 'against'"
    ).fetchone()[0]

    user_vote = None
    if g.get('user'):
        row = db.execute(
            'SELECT stance FROM union_vote WHERE user_id = ?',
            (g.user['id'],)
        ).fetchone()
        if row:
            user_vote = row['stance']

    return dict(
        union_for_count=for_count,
        union_against_count=against_count,
        union_user_vote=user_vote
    )
