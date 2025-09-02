#!/usr/bin/env python3
"""
Test script to verify that all imports work correctly in the Docker containers
"""

def test_preprocessor_imports():
    print("Testing preprocessor imports...")
    try:
        # Test the problematic import
        from utils.cleaner import Cleaner
        print("✅ utils.cleaner import successful")
        
        # Test other imports from app directory
        from app.subscriber.sub_kafka_configurations import ConsumerConfig
        from app.publisher.pub_kafka_configurations import ProducerConfig
        from app.update_data import Update
        print("✅ All preprocessor imports successful")
        return True
    except ImportError as e:
        print(f"❌ Preprocessor import failed: {e}")
        return False

def test_enricher_imports():
    print("Testing enricher imports...")
    try:
        # Test the problematic imports
        from utils.cleaner import Cleaner
        from app.weapon_processing.weapons_loader import load_weapons_data
        print("✅ utils.cleaner and weapons_loader imports successful")
        
        # Test other imports from app directory
        from app.subscriber.sub_kafka_configurations import ConsumerConfig
        from app.publisher.pub_kafka_configurations import ProducerConfig
        print("✅ All enricher imports successful")
        return True
    except ImportError as e:
        print(f"❌ Enricher import failed: {e}")
        return False

if __name__ == "__main__":
    import sys
    import os
    
    service = os.getenv('SERVICE_NAME', 'unknown')
    
    if service == 'preprocessor':
        success = test_preprocessor_imports()
    elif service == 'enricher':
        success = test_enricher_imports()
    else:
        print(f"Unknown service: {service}")
        success = False
    
    sys.exit(0 if success else 1)