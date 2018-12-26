from setuptools import setup, find_packages

setup(
    name='Pre-commit hook for protected branches',
    entry_points={
        'console_scripts': [
            'pre-commit-protected-branch = pre_commit_protected_branch.protected_branch:main'
        ]
    }
)
