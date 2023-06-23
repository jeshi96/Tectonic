CXX := g++
CXXFLAGS := -std=c++11

all: tree-clusters tree-clusters-parameter tree-clusters-parameter-no-mixed

tree-clusters: tree-clusters.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

tree-clusters-parameter: tree-clusters-parameter.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

tree-clusters-parameter-no-mixed: tree-clusters-parameter-no-mixed.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

clean:
	rm -f tree-clusters tree-clusters-parameter tree-clusters-parameter-no-mixed
