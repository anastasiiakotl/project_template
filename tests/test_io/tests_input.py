import unittest
import pandas as pd
from app.io.input import read_from_file_native, read_from_file_with_pandas


class TestReadFromFileNative(unittest.TestCase):

    def test_read_file_exists(self):
        result = read_from_file_native('C:/Users/Anastasiia/PycharmProjects/project_template/data/input.txt')
        self.assertIsNotNone(result)

    def test_read_file_content(self):
        expected_content = "hello world"
        result = read_from_file_native('C:/Users/Anastasiia/PycharmProjects/project_template/data/input.txt')
        self.assertEqual(result, expected_content)

    def test_read_file_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_native('data/nonexistent_file.txt')


class TestReadFromFileWithPandas(unittest.TestCase):

    def test_read_existing_csv_file(self):
        file_path = "C:/Users/Anastasiia/PycharmProjects/project_template/data/input.csv"
        result = read_from_file_with_pandas(file_path)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, pd.DataFrame)

    def test_read_file_pandas_content(self):
        expected_columns = ['greeting']
        expected_data = [[' hello'], [' world']]
        result = read_from_file_with_pandas('C:/Users/Anastasiia/PycharmProjects/project_template/data/input.csv')
        self.assertEqual(list(result.columns), expected_columns)
        self.assertListEqual(result.values.tolist(), expected_data)

    def test_read_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_with_pandas('C:/Users/Anastasiia/PycharmProjects/project_template/data/non_exist.csv')


if __name__ == '__main__':
    unittest.main()
