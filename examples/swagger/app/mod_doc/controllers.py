# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify

from flask.ext.autodoc import Autodoc

import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

doc = Blueprint('doc', __name__, url_prefix='/doc')
auto = Autodoc()



@doc.route('/swagger')
def swagger():
    ag = auto.generate()
    ret = []
    for a in ag:
        del(a['args'])
        pp.pprint(a)
        ret.append(a)

    return json.dumps(ret) #auto.html(template="swagger.json")

@doc.route('/')
@doc.route('/public')
def public_doc():
    return auto.html(title='Blog Documentation')


@doc.route('/private')
def private_doc():
    return auto.html(groups=['private'], title='Private Documentation')


@doc.route('/test')
@auto.doc()
def test():
    """Creates a new user.
    Form Data: username.
    """
    return "test"


@doc.route('/site/<int:site>', methods=['POST',"GET"])
@auto.doc()
def testInt(site, *args, **kwargs):
    return "<pre>" + site + "</pre>"

@doc.route('/site/<string:site>', methods=['POST',"GET"])
@auto.doc()
def testStr(site, *args, **kwargs):
    return "<pre>" + site + "</pre>"

@doc.route('/test2', methods=['GET', 'POST'])
@auto.doc()
def test2():
    ''' 
    @GET
    @tags:["site_license"]
    @summary: "Generate site_license file"
    @description: "Generate site_license file"
    @operationId: "getLicenseBySite"
    @produces: ["application/json"]
    @parameters: [
      {
        "name": "site",
        "in": "path",
        "description": "ID of site to be fetched",
        "required": true,
        "type": "integer",
        "maximum": 20.0,
        "minimum": 1.0,
        "format": "int64"
      },
      {
        "name": "email",
        "in": "query",
        "description": "email of user for authenication",
        "required": true,
        "type": "string"
      },
      {
        "name": "packaging",
        "in": "query",
        "description": "Package type",
        "required": true,
        "type": "string",
        "enum": [
          "one",
          "server",
          "site",
          "pool"
        ]
      }
    ]
    @responses
    200:{
        "description": "successful operation, packaged license file for site returned as text",
        "schema": {
          "$ref": "#/definitions/Site"
        }
    401:{
        "description": "Invalid ID supplied"
        }
    404:{
        "description": "Site not found"
      }
    406: {
        "description": "invalid request ({f})"
      }
    407: {
        "description": "valid packaging: {p}"
      }
    408: {
        "description": "Invalid site '{s}'"
      }
    409: {
        "description": "Invalid email '{e}'"
      }
    410": {
        "description": "Email '{e}' not authorized for site {s}"
      }
        
    @POST
    @tags: ["site_report"]
    @summary: "Generate site_report"
    @description: "Generate site_report"
    @operationId: "getSiteReport"
    @produces: ["application/json"]
    @parameters: [
          {
            "name": "site",
            "in": "path",
            "description": "ID of site to be fetched",
            "required": true,
            "type": "integer",
            "maximum": 20.0,
            "minimum": 1.0,
            "format": "int64"
          },
          {
            "name": "email",
            "in": "formData",
            "description": "email of user for authenication",
            "required": true,
            "type": "string"
          },
          {
            "name": "form",
            "in": "formData",
            "description": "Package type",
            "required": true,
            "type": "string",
            "enum": [
              "json"
            ]
          }
        ],
    @responses
    200: {
        "description": "successful operation",
        "schema": {
          "$ref": "#/definitions/site_report"
        }
    },
    401: {
        "description": "Email '{e}' not authorized for site {s}"
    },
    404: {
        "description": "Site not found"
    },
    406: {
        "description": "invalid request ({f})"
    },
    407: {
        "description": "valid packaging: {p}"
    },
    408: {
        "description": "Invalid site '{s}'"
    }

    '''
    return "test2"