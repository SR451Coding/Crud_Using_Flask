from flask import Flask, render_template, request, redirect, url_for
from parts import get_parts, insert_parts, delete_parts, search_parts, update_parts
from report import product_vendor, vendor_report, product_report
from vendors import get_vendors, insert_vendors, delete_vendors, update_vendors, search_vendors, Assign_vendor, delete_vendors_availability
from dbconfig import config
import psycopg2

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    rows = get_parts()
    id = request.form.get("pid")
    if request.method == 'POST':
        vrows = vendor_report(id)
        prows = product_report(id)
        return render_template('product_availability.html', prows=prows, vrows=vrows)

    return render_template('home.html', rows=rows)


@app.route('/vendor')
def vendors():
    rows = get_vendors()
    return render_template('vendors.html', rows=rows)

@app.route('/new_vendor', methods=['GET', 'POST'])
def New_vendor():
    name = request.form.get("pname")
    if request.method == 'POST':
        insert_vendors(name)
        return render_template('alert.html', v_message="Vendor created successfully")
    return render_template('new_vendor.html')


@app.route('/delete_vendor/<int:id>', methods=['GET', 'POST'])
def delete_vendor(id):
        delete_vendors(id)
        return render_template('alert.html', v_message="deleted successfully")

@app.route('/update_vendor/<int:id>', methods=['GET', 'POST'])
def update_vendor(id):
    rows=search_vendors(id)
    if request.method == 'POST':
        name = request.form.get("pname")
        update_vendors(name,id)
        return render_template('alert.html', v_message="updated successfully")
    return render_template('update_vendor.html', rows=rows)

@app.route('/assign_vendor/<int:pid>', methods=['GET', 'POST'])
def assign_vendor(pid):
    prows = product_report(pid)
    vrows = get_vendors()
    if request.method == 'POST':
        vid = request.form.getlist("vendors")
        Assign_vendor(pid, vid)
        return redirect(url_for('parts'))
    return render_template('assign_vendor.html', prows=prows, vrows=vrows)


@app.route('/delete_vendor_availability/<int:vid>/<int:pid>', methods=['GET', 'POST'])
def Delete_vendors_availability(vid, pid):
    delete_vendors_availability(vid, pid)
    return redirect(url_for('home'))



@app.route('/parts', methods=['GET', 'POST'])
def parts():
    rows = get_parts()
    return render_template('parts.html', rows=rows)


@app.route('/new_part', methods=['GET', 'POST'])
def New_part():
    name = request.form.get("pname")
    if request.method == 'POST':
        insert_parts(name)
        return render_template('alert.html', p_message="created successfully")
    return render_template('new_part.html')


@app.route('/delete_part/<int:id>', methods=['GET', 'POST'])
def delete_part(id):
        delete_parts(id)
        return render_template('alert.html', p_message="deleted successfully")

@app.route('/update_part/<int:id>', methods=['GET', 'POST'])
def update_part(id):
    rows=search_parts(id)
    if request.method == 'POST':
        name = request.form.get("pname")
        update_parts(name,id)
        return render_template('alert.html', p_message="updated successfully")
    return render_template('update_part.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
