class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # given n airports connected by flights and an array flights where flights[i] = [from_i, to_i, price_i] which is a directed flight from airport to another airport for price_i cost. 
        # no duplicate flights and no flights to its own airport (a cycle).
        # given src airport, dst airport, and the max # of stops we can make excluding src and dst, k.
        # return the cheapest price from src to dst with at most k stops.
        # return -1 if impossible to get to dst within k stops.

        # we want to create an array that holds the cost to get to each airport from src. We first initialize these to float('inf') to minimize it.
        # src node gets initiaized to 0 since it doesnt cost anything. 
        # we can use bellman ford algo since were bounded to visit each node k times.

        prices = [float('inf')] * n
        prices[src] = 0
        # so we will iterate k + 1 times since were only counting stops and the final dest doesnt count as a stop.
            # then we will iterate over flights array and identify if the price of that flight from s == inf. if so that means weve never visited that airport and therefore cannot fly out of it. continue
            # if the cost to fly out of src airport + price < the price it takes to get to the dst stored in temp prices. we use temp so that each round reflects exactly one flight to its path.
        for _ in range(k+1):
            tempPrices = prices.copy()

            for s, d, cost in flights:
                if prices[s] == float('inf'):
                    continue
                if prices[s] + cost < tempPrices[d]:
                    tempPrices[d] = prices[s] + cost
        # then we update our real prices arr to reflect the temp. 
        
            prices = tempPrices

        # then we return -1 if prices[dst] == inf, otherwise return prices[dst]
        return -1 if prices[dst] == float('inf') else prices[dst]