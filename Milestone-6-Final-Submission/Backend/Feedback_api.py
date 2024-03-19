from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, Api
from model import db, Feedback, Ticket, User


class Feedback_api(Resource):
    @jwt_required()
    def get(self, ticket_id=None, feedback_id=None):
        if feedback_id:
            feedback = Feedback.query.get(feedback_id)
            if not feedback:
                return {"error": "Feedback not found"}, 404
            return {
                "feedback_id": feedback.feedback_id,
                "ticket_id": feedback.ticket_id,
                "user_id": feedback.user_id,
                "content": feedback.content,
            }, 200
        elif ticket_id:
            feedbacks = Feedback.query.filter_by(ticket_id=ticket_id).all()
        else:
            feedbacks = Feedback.query.all()

        feedback_list = [
            {
                "feedback_id": feedback.feedback_id,
                "ticket_id": feedback.ticket_id,
                "user_id": feedback.user_id,
                "content": feedback.content,
            }
            for feedback in feedbacks
        ]
        return {"feedback": feedback_list}, 200


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


    @jwt_required()
    def put(self, feedback_id):
        username = get_jwt_identity()
        feedback_data = request.get_json()
        feedback = Feedback.query.get(feedback_id)

        if not feedback:
            return {"error": "Feedback not found"}, 404

        user = User.query.filter_by(username=username).first()

        if feedback.user_id != user.user_id:
            return {"error": "Unauthorized"}, 403

        feedback.content = feedback_data.get("content", feedback.content)
        db.session.commit()

        return {"message": "Feedback updated successfully !!"}, 200


    @jwt_required()
    def delete(self, feedback_id):
        username = get_jwt_identity()
        feedback = Feedback.query.get(feedback_id)

        if not feedback:
            return {"error": "Feedback not found"}, 404

        user = User.query.filter_by(username=username).first()
        if feedback.user_id != user.user_id:
            return {"error": "Unauthorized"}, 403

        db.session.delete(feedback)
        db.session.commit()

        return {"message": "Feedback deleted successfully"}, 200
