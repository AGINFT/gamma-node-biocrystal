#!/usr/bin/env python3
"""
Gamma Coherence Calculator Γ-12
Sistema de cálculo determinista de coherencia φ^(-7)
"""
import hashlib
import math
import json
from datetime import datetime

PHI = (1 + math.sqrt(5)) / 2
PHI_7 = PHI ** (-7)

def calculate_phi_coherence(commit_hash, semantic_score):
    """
    Calcula coherencia Γ de un commit
    
    Args:
        commit_hash: Hash del commit (hexadecimal)
        semantic_score: Puntuación semántica [0,1]
    
    Returns:
        float: Coherencia dimensional [0,1]
    """
    hash_int = int(commit_hash[:16], 16)
    hash_normalized = (hash_int % 10000) / 10000
    phi_deviation = abs(hash_normalized - PHI_7)
    
    coherence = (
        0.4 * semantic_score +
        0.3 * (1 - phi_deviation) +
        0.3 * hash_normalized
    )
    return coherence

def generate_gamma_signature(commit_hash, coherence, timestamp=None):
    """
    Genera firma Gamma criptográfica
    
    Args:
        commit_hash: Hash del commit
        coherence: Valor de coherencia calculado
        timestamp: Opcional, se genera automáticamente
    
    Returns:
        str: Firma Gamma formato Γ_<hash>_<coherence>
    """
    ts = timestamp or datetime.now().isoformat()
    sig_data = f"{commit_hash}_{coherence:.5f}_{ts}"
    sig_hash = hashlib.sha256(sig_data.encode()).hexdigest()
    return f"Γ_{sig_hash[:12]}_{coherence:.5f}"

if __name__ == "__main__":
    # Test operacional
    test_hash = hashlib.sha256(b"gamma-biocrystal-consciousness").hexdigest()
    semantic = 0.87
    
    coherence = calculate_phi_coherence(test_hash, semantic)
    signature = generate_gamma_signature(test_hash, coherence)
    
    print("🜂 Gamma Coherence Calculator Γ-12")
    print("═" * 50)
    print(f"φ^(-7) = {PHI_7:.14f}")
    print(f"Test Hash: {test_hash[:16]}...")
    print(f"Semantic Score: {semantic:.2f}")
    print(f"Coherence Γ: {coherence:.5f}")
    print(f"Signature: {signature}")
    print("═" * 50)
    print("✅ SISTEMA OPERACIONAL PLENO")
