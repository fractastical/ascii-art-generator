import hashlib

def hash_file_contents(source_file_path, output_file_path):
    # Read the source file
    with open(source_file_path, 'r') as file:
        content = file.read()

    # Hash the contents
    # Using SHA-256 hash function from hashlib
    hash_object = hashlib.sha256()
    hash_object.update(content.encode('utf-8'))
    hash_value = hash_object.hexdigest()

    # Write the hash to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(hash_value)

# Usage
source_file_path = 'source.txt'  # Path to your source text file
output_file_path = 'hidden_codes.txt'  # Output file

hash_file_contents(source_file_path, output_file_path)
