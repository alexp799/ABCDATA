# -*- coding: utf-8 -*-
from app import app
from app import models
from app.models import SModel
from flask import render_template, request, url_for,jsonify
import os
import flask
import os
# TODO:
# abc.ru/api/000009111/
# REST API

@app.route('/')
@app.route('/index')
def index(page=1):
    page = request.args.get('page', 1, type=int)
    objs = SModel.query.paginate(
        page, app.config['OBJECTS_PER_PAGE'], False)
    next_url = url_for('index', page=objs.next_num) \
        if objs.has_next else None
    prev_url = url_for('index', page=objs.prev_num) \
        if objs.has_prev else None
    return render_template('index.html', title='Home',
                           objs=objs.items, next_url=next_url,
                           prev_url=prev_url)


@app.route('/second/<current_object_name>')
def second(current_object_name):
	
	obj = SModel.query.filter_by(name=current_object_name).first_or_404()
	
	return render_template('second.html', obj=obj)

@app.route('/abc/api/<string:model_name>/info', methods=['GET'])
def get_info(model_name):
    ourmodel=SModel.query.filter_by(name=model_name).first()
    filestr=''
    if not ourmodel:
        return jsonify('no model with name: '+model_name)
    l1=len(ourmodel.path)
    l2=len(ourmodel.name)
    for root,dirs,files in os.walk('app/'+ourmodel.path[:l1-l2-1]):
      for filename in files:
        filestr=filestr+filename+'\n'

    return jsonify(filestr)

@app.route('/abc/api/<string:model_name>/<string:type>', methods=['GET'])
def get_tasks(model_name,type):
    ourmodel=SModel.query.filter_by(name=model_name).first()
    if not ourmodel:
        return jsonify('no model with name: '+model_name)

    return flask.send_file(ourmodel.path+'.'+type)
