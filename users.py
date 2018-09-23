import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def register():
  return 'Should register a user'