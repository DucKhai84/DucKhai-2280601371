from flask import Flask, request, jsonify
from cipher.rsa import RSACipher
from cipher.ecc import ECCCipher
app = Flask(__name__)
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing message parameter'}), 400
    
    message = data['message']
    key_type = data.get('key_type', 'public')

    private_key, public_key = rsa_cipher.load_keys()
    key = public_key if key_type == 'public' else private_key

    if key is None:
        return jsonify({'error': 'Invalid or missing key'}), 400

    try:
        encrypted_message = rsa_cipher.encrypt(message, key)
        return jsonify({'encrypted_message': encrypted_message.hex()})
    except Exception as e:
        return jsonify({'error': f'Encryption failed: {str(e)}'}), 500

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.get_json()
    if not data or 'ciphertext' not in data:
        return jsonify({'error': 'Missing ciphertext parameter'}), 400
    
    ciphertext_hex = data['ciphertext']
    key_type = data.get('key_type', 'private')

    private_key, public_key = rsa_cipher.load_keys()
    key = private_key if key_type == 'private' else public_key

    if key is None:
        return jsonify({'error': 'Invalid or missing key'}), 400

    try:
        decrypted_message = rsa_cipher.decrypt(bytes.fromhex(ciphertext_hex), key)
        return jsonify({'decrypted_message': decrypted_message})
    except Exception as e:
        return jsonify({'error': f'Decryption failed: {str(e)}'}), 400

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing message parameter'}), 400
    
    message = data['message']

    private_key, _ = rsa_cipher.load_keys()
    if private_key is None:
        return jsonify({'error': 'Private key not found'}), 400

    try:
        signature = rsa_cipher.sign(message, private_key)
        return jsonify({'signature': signature.hex()})
    except Exception as e:
        return jsonify({'error': f'Signing failed: {str(e)}'}), 500

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify_signature():
    data = request.get_json()
    if not data or 'message' not in data or 'signature' not in data:
        return jsonify({'error': 'Missing message or signature parameter'}), 400
    
    message = data['message']
    signature_hex = data['signature']

    public_key, _ = rsa_cipher.load_keys()
    if public_key is None:
        return jsonify({'error': 'Public key not found'}), 400

    try:
        is_verified = rsa_cipher.verify(message, bytes.fromhex(signature_hex), public_key)
        return jsonify({'is_verified': is_verified})
    except Exception as e:
        return jsonify({'error': f'Verification failed: {str(e)}'}), 400





# Thêm đoạn này trước hàm main
# ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key, _ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
