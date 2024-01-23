import localstack_client.session as boto3
import botocore
from prettytable import PrettyTable


def search_files_in_s3_bucket(bucket_name: str, substring: str):
    """_summary_
        Searches the substring in the specified S3 bucket. 
    Args:
        bucket_name (str): name of the bucket
        substring (str): substring to search in all files inside bucket
    Returns:
        list[str] : Two Lists -  One with the files containing and another that does not contians the substring
    """

    # get the S3 resource
    s3 = boto3.client('s3')
    # initialize empty lists
    file_names_with_substring = []
    file_names_without_substring = []

    try:
        # Check if bucket exists
        s3.head_bucket(Bucket=bucket_name)

        # Iterate through S3 bucket objects
        for obj in s3.list_objects(Bucket=bucket_name)['Contents']:
            file_key = obj['Key']

            # Check if the object is a text file
            if file_key.lower().endswith('.txt'):
                # Read file content
                file_content = s3.get_object(Bucket=bucket_name, Key=file_key)[
                    'Body'].read().decode('utf-8')

                # Check if substring is present in file content
                if substring in file_content:
                    file_names_with_substring.append(file_key)
                else:
                    file_names_without_substring.append(file_key)

    except botocore.exceptions.ClientError as err:
        raise err

    return file_names_with_substring, file_names_without_substring


def add_lists_to_pretty_table(with_substring: list, without_substring: list):
    """_summary_
        Adds the lists in the pretty_table
    Args:
        with_substring (list): list of files that contiains the substring
        without_substring (list): list of files that do not contiains the substring
    Returns:
        pretty_table : returns the listis structed in the pretty_table
    """
    # initialize prettytable
    output_table = PrettyTable(["File_Name", "Substring"])

    # Append the files which contains the substring to search in the pretty_table
    for found in with_substring:
        output_table.add_row([found, "Found"])

    # Append the files which DOES NOT contains the substring to search in the pretty_table
    for not_found in without_substring:
        output_table.add_row([not_found, "Not Found"])

    # Align the pretty_table colums to left
    output_table.align = "l"
    return output_table


def main():

    try:
        # Get the indtended bucket name and the substring to search as an Input from the user
        bucket_name = input('Bucket Name: ')
        search_substring = input('Substring to search: ')

        with_substring, without_substring = search_files_in_s3_bucket(
            bucket_name, search_substring)

        result_table = add_lists_to_pretty_table(with_substring, without_substring)
        print(result_table)

    except ValueError as ve:
        print({ve})
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    main()
