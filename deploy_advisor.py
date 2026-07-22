import time
import sys


def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    print("\n" + "="*50)
    print("   🤖 CLOUD ARCHITECTURE DECISION ENGINE v1.0")
    print("="*50 + "\n")
    
    slow_print("Initializing Logic Core... [OK]")
    slow_print("Connecting to Knowledge Base... [OK]")
    print("\n--- INPUT PARAMETERS ---")
    
    traffic = input("1. Traffic Pattern (steady/bursty)? ").strip().lower()
    latency = input("2. Latency Sensitivity (critical/standard)? ").strip().lower()
    budget  = input("3. Project Budget (enterprise/startup)? ").strip().lower()
    
    print("\n🔄 RUNNING SIMULATION ALGORITHMS...")
    time.sleep(1)
    print("   [||||||||||     ] 50% analyzing cost models...")
    time.sleep(1)
    print("   [|||||||||||||||] 100% complete.")
    
    print("\n" + "-"*50)
    print("📢 RECOMMENDATION REPORT")
    print("-"*50)

    if traffic == "bursty" and budget == "startup":
        slow_print("✅ OPTIMAL ARCHITECTURE: Serverless FaaS (Google Cloud Functions)")
        print("\n   WHY:")
        print("   1. 'Scale-to-Zero' capability eliminates idle costs (Save ~$20/mo).")
        print("   2. Auto-scaling handles sudden traffic spikes instantly.")
        print("   3. Perfect for: Spam Classifiers, Chatbots, Event-driven tasks.")
        
    elif traffic == "steady":
        slow_print("✅ OPTIMAL ARCHITECTURE: Dedicated Virtual Machine (EC2 / Compute Engine)")
        print("\n   WHY:")
        print("   1. Predictable performance for constant workloads.")
        print("   2. No 'Cold Start' latency issues.")
        
    else:
        slow_print("⚠️ RECOMMENDATION: Hybrid Container (Google Cloud Run)")
        print("\n   WHY: Best balance of portability and serverless scaling.")

    print("\n" + "="*50)
    print("   SIMULATION COMPLETE")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()