# muoncoincidenceMC

Simple Monte Carlo predictor for muon detection coincidence counters

The muon incidence angle distribution can be appropriately modelled by a cos^2 distribution. This has been used to run a simple Monte Carlo program to predict the expected muon count from a muon coincidence detector. Muons travelling in enough of a downward direction will pass through both detectors, and record a coincidence event. Muons of a more horizontal path will miss the second detector and thus not record a count. 

Simple trigonometry is enough to track the path of a randomly generated muon from detector 1 to detector 2. Repeated simulation can give an approximate idea of the expected counts for a detector of given size and efficiency.
