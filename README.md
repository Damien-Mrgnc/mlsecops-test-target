# mlsecops-test-target

Repo de démonstration pour l'agent [mlsecops-ai-reviewer](https://github.com/Damien-Mrgnc/mlsecops-ai-reviewer).

Chaque Pull Request ouverte sur ce repo déclenche automatiquement une review IA qui analyse le diff, détecte les vulnérabilités, et bloque le merge si des règles de sécurité sont violées.

---

## Rôle dans le système MLSecOps

```
mlsecops-ai-reviewer        mlsecops-test-target
      (agent)          →→→       (cible)
                              PRs ouvertes ici
                              déclenche ai-review.yml
                              l'agent checkout le reviewer
                              analyse le diff
                              poste APPROVE / REQUEST_CHANGES
```

Ce repo existe pour démontrer le fonctionnement de l'agent en conditions réelles — les PRs sont intentionnellement bonnes ou mauvaises pour valider les deux chemins.

---

## Règles de review (`.reporules`)

Les règles appliquées sur ce repo :

```markdown
## Sécurité (CRITIQUE)
- INTERDICTION de hardcoder des secrets, clés API ou mots de passe.
- INTERDICTION de désactiver SSL (verify=False).
- Les requêtes SQL DOIVENT utiliser des paramètres préparés.

## Qualité (AVERTISSEMENT)
- Les noms de variables DOIVENT être descriptifs.
- Les exceptions DOIVENT être catchées spécifiquement.
```

---

## Tester l'agent

Ouvrir une PR avec du code violant les règles :

```python
# Exemple — déclenche REQUEST_CHANGES
import requests
API_KEY = "sk-prod-abc123"            # hardcoded secret → CRITIQUE
r = requests.get(url, verify=False)   # SSL désactivé → CRITIQUE
```

L'agent postera automatiquement une review et bloquera le merge.

---

## Liens

- [mlsecops-ai-reviewer](https://github.com/Damien-Mrgnc/mlsecops-ai-reviewer) — code de l'agent
- [aws-mlsecops-infrastructure](https://github.com/Damien-Mrgnc/aws-mlsecops-infrastructure) — infrastructure AWS du système MLSecOps
