import os
import subprocess
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GUMROAD_TOKEN = os.getenv('GUMROAD_TOKEN')

OPENCLAW_REPO = 'https://github.com/openclaw/openclaw.git'
LOCAL_PATH = './openclaw'

class CompletePipeline:
    def run_cmd(self, cmd, cwd=None):
        print(f'🚀 → {" ".join(cmd)}')
        result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print('❌ Error:', result.stderr)
            raise Exception(result.stderr)
        print(result.stdout.strip() or '✅ Done')
        return result.stdout.strip()

    def setup_openclaw(self):
        print('\n🔄 OPENCLAW SETUP')
        if os.path.exists(LOCAL_PATH):
            self.run_cmd(['git', 'pull', 'origin', 'main'], cwd=LOCAL_PATH)
        else:
            self.run_cmd(['git', 'clone', OPENCLAW_REPO, LOCAL_PATH])
        self.run_cmd(['pnpm', 'install'], cwd=LOCAL_PATH)
        self.run_cmd(['pnpm', 'update'], cwd=LOCAL_PATH)
        self.run_cmd(['pnpm', 'build'], cwd=LOCAL_PATH)
        print('✅ OpenClaw ready!')

    def run(self):
        print('🎉 PLP LLC Multi-Agent Pipeline Ready!')
        print('Repo: https://github.com/TankEastCoast91/plp-llc-launch-kit')

if __name__ == '__main__':
    CompletePipeline().run()