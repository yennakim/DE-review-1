import os
from dotenv import load_dotenv
from api import get_and_save_data

load_dotenv()

def read_env_variable():
  NAME = os.getenv('CONTRIBUTOR')
  print(NAME)


def main():
  read_env_variable()
  get_and_save_data()


if __name__ == "__main__":
  main()