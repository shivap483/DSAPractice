import hashlib
import os


def sample_hash_file(current_path):
    no_of_bytes_to_read_per_sample = 4000
    total_bytes = os.path.getsize(current_path)
    hasher = hashlib.sha512()
    with open(current_path, 'rb') as file:
        if total_bytes < no_of_bytes_to_read_per_sample:
            hasher.update(file.read())
        else:
            bytes_between_samples = (total_bytes - no_of_bytes_to_read_per_sample * 3) / 2

            for offset_multiplier in range(3):
                start_of_sample = (offset_multiplier * (bytes_between_samples + no_of_bytes_to_read_per_sample))
                file.seek(start_of_sample)
                sample = file.read(no_of_bytes_to_read_per_sample)
                hasher.update(sample)
        return hasher.hexdigest()


def find_duplicate_files(starting_directory):
    visited_files = {}
    directory_stack = [starting_directory]
    duplicates = []

    while len(directory_stack) > 0:
        current_path = directory_stack.pop()
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
            directory_stack.append(full_path)
        else:
            file_hash = sample_hash_file(current_path)
            current_last_edited_time = os.path.getmtime(current_path)
            if file_hash in visited_files:
                existing_last_edited_time, existing_path = visited_files[file_hash]
                if current_last_edited_time > existing_last_edited_time:
                    duplicates.append((current_path, existing_path))
                else:
                    duplicates.append((existing_path, current_path))
                    visited_files[file_hash] = (current_last_edited_time, current_path)
            else:
                visited_files[file_hash] = (current_last_edited_time, current_path)
    return duplicates
