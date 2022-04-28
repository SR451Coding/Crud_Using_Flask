from flask import Flask, render_template, request, redirect, url_for
from vendors import get_vendors
from __main__ import app


@app.route('/vendor')
def vendors():
    rows = get_vendors()
    return render_template('vendors.html', rows=rows)