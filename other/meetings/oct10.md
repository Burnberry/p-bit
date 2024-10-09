# To Do
- BM wat meer opzoeken
  - Focus op implementatie met simulated bifurcation i.p.v. sim. annealing
  - Code zoeken voor DBM contrastive divergence (git) (en opzoeken I guess)
- nadenken over uiteindelijk doel
- voorbeeld mnist via p-bits doornemen
- doornemen quantum rl als er tijd is?
- refs
  - https://arxiv.org/pdf/2303.10728 (MNIST p-bit BM voorbeeld)
  - https://arxiv.org/pdf/1612.05695 (quantum RL)
  - https://www.nature.com/articles/s41598-024-51639-x (wrm sim. annealing niet goed is)
  - https://scikit-learn.org/stable/auto_examples/neural_networks/plot_rbm_logistic_classification.html (Bm scikit speelruitme?)

# Plan
- Hoe p-bit connecteren in RL verhaal

# To discuss
- MNIST paper (Training Deep Boltzmann Networks with Sparse Ising Machines)
  - algo:
    - Model + image bias -> sample via p-bits
    - sample model
    - pass weights aan via formules
  - persistent cd: start vanaf vorige sample state
  - visible bits: image + label split voor generation/classification

- RL
  - nog op te frissen zit ver, moet zelf nog zoeken

- plan
  - reinforcement learning herbekijken + quantum voorbeeld
  - RBM/DBM experimenten proberen
    - gibbs sampling alsof het met p-computer is, maar met cpu berekenen
    - uitzoeken connectie RL
# Meeting Notes
- 