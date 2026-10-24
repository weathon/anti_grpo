import requests, subprocess
session = requests.Session()
session.trust_env = False
r = session.get("http://127.0.0.1:5000/", params={"path": "2235.jpg", "prompt": "a outdoor field"}, timeout=300)
print("hps", r.status_code, r.text[:200])
print(subprocess.run(["nvidia-smi", "--query-compute-apps=pid,used_memory", "--format=csv"], capture_output=True, text=True).stdout)
print(subprocess.run(["grep", "-c", "add_generation_prompt=True", "/usr/local/lib/python3.13/dist-packages/trl/trainer/grpo_trainer.py"], capture_output=True, text=True).stdout)
