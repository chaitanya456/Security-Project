from lxml import etree
from flask import Flask, request

app = Flask(__name__)

@app.route('/xml', methods=['POST'])
def xml_endpoint():
    xml_data = request.data
    try:
        # Allow network entities, and ensure DTD is loaded for reading local files
        parser = etree.XMLParser(resolve_entities=True, no_network=False, load_dtd=True)
        root = etree.fromstring(xml_data, parser)
        return f"Parsed: {etree.tostring(root, pretty_print=True).decode()}"
    except Exception as e:
        return f"Error: {str(e)}", 400

@app.route('/admin', methods=['GET'])
def admin_service():
    return "Secret Admin Panel Data"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)  # <-- Make sure it's 0.0.0.0
