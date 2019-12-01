import os
from flask import Flask, jsonify, request
from recommender import Recommender

application = Flask("recommender")
recommender = Recommender.load(os.environ.get("MODEL_PATH"))

@application.route("/recommend/<int:user_id>")
def recommend(user_id):
  limit = int(request.args.get('limit', 50))
  recommendations = recommender.recommend_for_user(user_id, limit)
  return jsonify(recommendations)

@application.route("/similar/<int:post_id>")
def similar(post_id):
  limit = int(request.args.get('limit', 50))
  recommendations = recommender.recommend_for_post(post_id, limit)
  return jsonify(recommendations)