from flask import Blueprint, request, jsonify
from app.utils import process_voice, process_image
from app.llm_model import get_llm_response

main_routes = Blueprint("main", __name__)

@main_routes.route("/query", methods=["POST"])
def query():
    data = request.json
    text_query = data.get("text")
    voice_file = data.get("voice_file")
    image_file = data.get("image_file")
    metadata = data.get("metadata")

    if voice_file:
        text_query = process_voice(voice_file)
    disease_info = None
    if image_file:
        disease_info = process_image(image_file)
    answer = get_llm_response(text_query, disease_info, metadata)
    return jsonify({"answer": answer})
