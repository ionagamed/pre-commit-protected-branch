from setuptools import setup

setup(
    name='Pre-commit hook for protected branches',
    entry_points={
        'console_scripts': [
            'pre-commit-protected-branch = pre_commit_hooks.protected_branch:main'
        ]
    }
)
