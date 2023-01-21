---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(myst-content/proofs-algorithms)=
# Problem 1: Linear map takes zero vector to zero vector

```{admonition} Problem 1

Let $T: V \rightarrow W$ be a linear map from vector space $V$ to $W$. Then

```{math}
T(0_{V})=0_{W}.

```

```{admonition} Solution
:class: hint, dropdown

$0_{V} + 0_{V} = 0_{V}.$ 

Thus, $T(0_{V} + 0_{V}) = T(0_{V})$ which is equal to $T(0_{V}) + T(0_{V}) = T(0_{V})$ given linearity of $T.$

Adding $-T(0_{V})$ on both sides yields $T(0_{V}) = 0_{W}$

```


