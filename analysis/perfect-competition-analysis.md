# Perfect Competition Farm Planning Analysis

*Draft, first pass. Numbers and logic are solid; still smoothing transitions and vocabulary in a few spots.*

When I first sat down with this model, my instinct was to check whether the plan made sense bed by bed rather than just trust the output. That's where the tomato numbers turned out to matter most.

Tomatoes bring in $8,800 per bed, and that's the number every other bed gets compared against. At bed 10, marginal cost is about $8,249, still below the $8,800 price, so that bed is still profitable at the margin. At bed 11, marginal cost jumps to about $9,391, now above the price, so that bed isn't worth planting. Bed 10 is basically where price and marginal cost meet, close enough to call it the profit-maximizing stopping point, even though the two numbers aren't perfectly equal.

Both carrots and mesclun are maxed out, carrots at 20 of 20 beds and mesclun at 30 of 30, so these are the caps actually limiting the plan. At bed 20, carrot marginal cost is about $1,742, still about $352 below its $2,094 price, meaning there's real value trapped behind the limit. Mesclun only has about $246 of value left at its cap. Since carrots have more value trapped behind the limit than mesclun does, loosening the carrot cap would help more. As for the other two potential constraints, total beds at 64 aren't binding, we have room there. Temp workers aren't worth relaxing either, we already have all 4 we'd need and there's slack left in the hours, so a fifth worker wouldn't change anything. Neither constraint is worth prioritizing.

*[FIGURE 2 PLACEHOLDER: Carrot Marginal Cost vs. Price chart — shows the binding cap at bed 20 and the value still trapped behind it]*

Farmer labor costs $34.72 an hour, temp labor costs $17.36 an hour. Around bed 6, the marginal labor being used shifts more toward the cheaper temp workers, and that wage difference is big enough to actually pull marginal cost down for a bit. But that's temporary, because labor requirements are compounding at 10 percent per bed. Eventually that growth outpaces the savings from cheaper labor, and marginal cost starts climbing again. That's what causes the dip in the curve.

*[FIGURE 1 PLACEHOLDER: Tomato Marginal Cost vs. Price chart — shows the P ≈ MC crossing around bed 10 and the labor-driven dip in the curve]*

Here's the piece that needed sharpening. Each crop looks unprofitable if you compare it against the full $20,000 fixed cost, but that cost gets paid no matter what we plant, so it's not the right comparison. The real question is whether price covers average variable cost. When price is above AVC, the crop is paying for all its own variable costs and still has something left over to put toward that unavoidable fixed cost, so it's worth growing even if it looks like a loss on paper. In this model, price does cover AVC for carrots and mesclun, which is why planting them still makes sense even though neither one looks profitable standalone.

My original guess was 20 tomatoes, 20 carrots, 24 mesclun. The model landed on 10, 20, 30. I was right that carrots would max out, but wrong about tomatoes and mesclun. Before I even built the model, I said I'd be wrong if it came in below 17 tomato beds. It landed on 10, so by my own standard I was clearly wrong about tomatoes. I knew tomato labor compounded at 10 percent, but I underestimated how much that would drag marginal cost up as beds increased. I also assumed all 64 beds should be used, but the optimal plan only uses 60. That's the real lesson here, filling every bed isn't the same as maximizing profit.
