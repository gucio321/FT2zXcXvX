# This is a documentation template

## You can write math formulas

$$
\int_a^b f(x) = \lim_{n\to\infty} \left(\frac{b-a}{n} * \sum_{i=1}^n f\left(a + i * \frac{b-a}{n}\right)\right)
$$

### Extended equations

```{math}
:label: pitagoras

a^2 + b^2 = c^2
```

You can refer this now {eq}`pitagoras`.

Also to be honest I breffer this `$$`-like syntax:

$$
\frac{a_1^3}{a_2^3} = \frac{T_1^2}{T_2^2}
$$ (eq2)

It also can have label {eq}`eq2`

## Plots

Yu can embed plots in markdown!

For full documentation see [here](https://github.com/gucio321/sphinxcontrib-plot)

```{plot} gnuplot
:caption: Przykładowy wykres
:size: 300,200

plot sin(x), cos(x)
```

## Graphs

This plot library also supports graphs

```{plot} dot -Tpng
:caption: Some graph

digraph G {
    subgraph cluster_0 {
            style=filled;
            color=lightgrey;
            node [style=filled,color=white];
            a0 -> a1 -> a2 -> a3;
            label = "process #1";
    }

    subgraph cluster_1 {
            node [style=filled];
            b0 -> b1 -> b2 -> b3;
            label = "process #2";
            color=blue
    }
    start -> a0;
    start -> b0;
    a1 -> b3;
    b2 -> a3;
    a3 -> a0;
    a3 -> end;
    b3 -> end;

    start [shape=Mdiamond];
    end [shape=Msquare];
}
