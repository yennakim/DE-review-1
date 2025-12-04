import os
from dotenv import load_dotenv

load_dotenv()

def read_env_variable():
  NAME = os.getenv('CONTRIBUTOR')
  print(NAME)

def main():
  read_env_variable()
  

if __name__ == "__main__":
  main()