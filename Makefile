default: fresh

# Sugeneruoti straipsnį.
article.pdf:
	xelatex -no-pdf main.tex
	xelatex -no-pdf main.tex
	xdvipdfmx main.xdv
	mv main.pdf article.pdf

fresh: clear article.pdf

# Išvalyti šiukšles.
clean:
	rm -f *.aux *.log *.xdv *.out *.toc

# Ištrinti visus sugeneruotus failus.
clear: clean
	rm -f *.pdf
