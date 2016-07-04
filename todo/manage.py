import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
