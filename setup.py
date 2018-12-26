from setuptools import setup, find_packages

setup(
    name='pre_commit_protected_branch',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pre-commit-protected-branch = pre_commit_protected_branch.protected_branch:main'
        ]
    }
)
