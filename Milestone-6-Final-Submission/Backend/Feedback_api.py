from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, Api
from model import db, Feedback, Ticket, User


class Feedback_api(Resource):
    @jwt_required()
    def post(self, ticket_id=None):
        if not ticket_id:
            return {"error": "Ticket ID is required for posting feedback!"}, 400

        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()

        if not user:
            return {"error": "User not found !!"}, 404

        data = request.get_json()
        content = data.get("content")

        if not content:
            return {"error": "Content is required !!"}, 400

        feedback = Feedback(ticket_id=ticket_id, user_id=user.user_id, content=content)

        db.session.add(feedback)
        db.session.commit()

        return {"message": "Feedback submitted successfully !!"}, 201