from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from fufo_main.auth import login_required
from fufo_main.db import get_db

bp = Blueprint('blog', __name__)