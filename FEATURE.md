<style>
r {color: Red}
o {color: Orange}
g {color: Green}
c {color: Cyan}
</style>

<h3>NOTE:</h3>

- Features marked <g>green</g> have been implemented, <o>orange</o> is work-in-progress and <r>red</r> has not yet been implemented.
- Blocks/Items marked <c>cyan</c>/<ins>underlined</ins> are modded and ``nano``/_italicised_ are vanilla.

## <o>Inventory</o>
### <o>Renaming</o>
- ``Block of Amethyst`` > <ins>Amethyst Block</ins>
    - ``Block of Coal`` > <ins>Coal Block</ins>
    - ``Block of Copper`` > <ins>Copper Block</ins>
    - ``Block of Raw Copper`` > <ins>Raw Copper Block</ins>
    - ``Block of Iron`` > <ins>Iron Block</ins>
    - ``Block of Raw Iron`` > <ins>Raw Iron Block</ins>
    - ``Block of Gold`` > <ins>Gold Block</ins>
    - ``Block of Raw Gold`` > <ins>Raw Gold Block</ins>
    - ``Block of Diamond`` > <ins>Diamond Block</ins>
    - ``Block of Emerald`` > <ins>Emerald Block</ins>
    - ``Block of Netherite`` > <ins>Netherite Block</ins>
    - ``Block of Quartz`` > <ins>Quartz Block</ins>
    - ``Block of Redstone`` > <ins>Redstone Block</ins>
    - ``Block of Resin`` > <ins>Resin Block</ins>
    - ``Block of Bamboo`` > <ins>Bamboo Block</ins>
    - ``Block of Stripped Bamboo`` > <ins>Stripped Bamboo Block</ins>
- ``End Stone`` > <ins>Endstone</ins>
    - ``End Stone Brick Slab`` > <ins>Endstone Brick Slab</ins>
    - ``End Stone Brick Stairs`` > <ins>Endstone Brick Stairs</ins>
    - ``End Stone Brick Wall`` > <ins>Endstone Brick Wall</ins>
    - ``End Stone Bricks`` > <ins>Endstone Bricks</ins>
- ``Polished Blackstone Brick Slab`` > <ins>Blackstone Brick Slab</ins>
    - ``Polished Blackstone Brick Stairs`` > <ins>Blackstone Brick Stairs</ins>
    - ``Polished Blackstone Brick Wall`` > <ins>Blackstone Brick Wall</ins>
    - ``Polished Blackstone Bricks`` > <ins>Blackstone Bricks</ins>
    - ``Chiseled Polished Blackstone`` > <ins>Chiseled Blackstone</ins>
    - ``Cracked Polished Blackstone Bricks`` > <ins>Cracked Blackstone Bricks</ins>
    - ``Polished Blackstone Button`` > <ins>Blackstone Button</ins>
    - ``Polished Blackstone Pressure Plate`` > <ins>Blackstone Pressure Plate</ins>
- ``Magma Block`` > <ins>Magma</ins>
- ``Soul Soil`` > <ins>Soul Sand</ins>
    - ``Soul Sand`` > <ins>Soul Soil</ins>
- ``Snow Block`` > <ins>Snow</ins>
    - ``Snow`` > <ins>Snow Layer</ins>
- ``Brick`` > <ins>Clay Brick</ins>
    - ``Bricks`` > <ins>Clay Bricks</ins>
- ``Dripstone Block`` > <ins>Dripstone</ins>
- ``Nether Wart Block`` > <ins>Crimson Wart Block</ins>
- ``Grass Block``> <ins>Grassy Dirt</ins>
- ``Azalea`` > <ins>Azalea Bush</ins>
    - ``Flowering Azalea`` > <ins>Flowering Azalea Bush</ins>
- ``Bottle O' Enchanting`` > <ins>Bottled Experience</ins>

### <o>Stacking</o>
- ``Horse Armour``, ``Saddle``, ``Minecart``, ``Boat``, Filled Buckets (``Water/Milk/Lava/Powder Snow Bucket``), Potions (``Regular/Splash/Lingering Potion``) now stacks to 16 (instead of 1)
- ``Empty Bucket``, ``Eye of Ender`` now stacks to 16 (instead of 64)
- ``Bed``, ``Cake``, ``Banner Pattern``, ``Disc``, ``Enchanted Book``, ``Water Bottle``, Ingredient Potions (``Awkward/Thick/Mundane Potion``), ``Soup/Stew``, ``Spyglass``, ``Goat Horn`` now stacks to 64 (instead of 1)
- ``Armour Stand``, ``Egg``, ``Snowball``, ``Sign``, ``Hanging Sign``, ``Honey Bottle`` now stacks to 64 (instead of 16)
- ``Splash Potion`` and ``Lingering Potion`` have a cooldown of 2 seconds upon usage

### <o>Storage Blocks</o>
- <c>Blazing Sand</c>: crafted from 9 ``Blaze Powder``, affected by gravity, deals damage on contact similar to ``Magma Block``
- <c>Glowing Sand</c>: crafted from 9 ``Glowstone Dust``, affected by gravity, emits light similar to ``Glowstone``
- <c>Magma Cream Block</c>: crafted from 9 ``Magma Cream``, behaves like ``Slime Block``, directional like _Logs_
- <c>Charcoal Block</c>: crafted from 9 ``Charcoal``, smelts 80 items in ``Furnace/Blast Furnace/Smoker`` similar to ``Coal Block``
- <c>Gunpowder Block</c>: crafted from 9 ``Gunpowder``, affected by gravity
- <c>Flintstone</c>: crafted from 9 ``Flint``, creates fire on flamable blocks when pushed/pulled besides ``Iron Block``
- <c>Amethyst Shard Block</c>: crafted from 9 ``Amethyst Shard``
- <c>Quartz Crystal Block</c>: crafted from 9 ``Nether Quartz``
- <c>Prismarine Shard Block</c>: crafted from 9 ``Prismarine Shard``
- <c>Prismarine Crystal Block</c>: crafted from 9 ``Prismarine Crystal``, emits light similar to ``Sea Lantern``
- <c>Echo Shard Block</c>: crafted from 9 ``Echo Shard``
- <c>Ender Pearl Block</c>: crafted from 9 ``Ender Pearl``
- <c>Netherite Scrap Heap</c>: crafted from 9 ``Netherite Scrap``
- <c>Sugar Cube</c>: crafted from 9 ``Sugar``, dissolves upon contact with _Water_, ``Snowball`` and ``Powdered Snow``
- <c>Sugarcane Block</c>: crafted from 9 ``Sugarcane``, has a chance to produce more <ins>Sugarcane Block</ins> when placed on ``Sand/Grass/Mud`` besides _Water_, directional like _Logs_
    - <c>Stripped Sugarcane Block</c>: obtained by stripping <ins>Sugarcane Block</ins> with any axe
    - (``Bamboo Block`` has a chance to produce more ``Bamboo Block`` when placed on ``Sand/Grass/Mud/Moss``)
    - (<ins>Stripped Sugarcane Block</ins>/``Stripped Bamboo Block`` do not produce more <ins>Sugarcane Block</ins>/``Bamboo Block``)
- (<ins>Crop Crates</ins>: new storage blocks for crops, directional like _Logs_)
    - <c>Apple Crate</c>: crafted from 9 ``Apple``
    - <c>Carrot Crate</c>: crafted from 9 ``Carrot``
    - <c>Beetroot Crate</c>: crafted from 9 ``Beetroot``
    - <c>Potato Crate</c>: crafted from 9 ``Potato``
    - <c>Chorus Fruit Crate</c>: crafted from 9 ``Chorus Fruit``
    - <c>Sweet Berry Crate</c>: crafted from 9 ``Sweet Berry``
    - <c>Glow Berry Crate</c>: crafted from 9 ``Glow Berry``
    - <c>Nether Wart Crate</c>: crafted from 9 ``Nether Wart``
- (<ins>Meat Barrels</ins>: new storage blocks for meats, directional like _Logs_)
    - <c>Salmon Barrel</c>: crafted from 9 ``Salmon``
    - <c>Cod Barrel</c>: crafted from 9 ``Cod``
    - <c>Pufferfish Barrel</c>: crafted from 9 ``Pufferfish``, deals Poison effect for 6 seconds on contact similar to ``Pufferfish``
    - <c>Tropical Fish Barrel</c>: crafted from 9 ``Tropical Fish``
    - <c>Pork Barrel</c>: crafted from 9 ``Raw Porkchop``
    - <c>Beef Barrel</c>: crafted from 9 ``Raw Beef``
    - <c>Mutton Barrel</c>: crafted from 9 ``Raw Mutton``
- <c>Egg Carton</c>: crafted from 9 ``Egg``, behaves like a slab
- <c>Rotten Flesh Heap</c>: crafted from 9 ``Rotten Flesh``
- <c>Leather Heap</c>: crafted from 9 ``Leather``
- <c>String Spool</c>: crafted from 9 ``String``, directional like _Logs_
- <c>Armadillo Scute Heap</c>: crafted from 9 ``Armadillo Scute``
- <c>Turtle Scute Heap</c>: crafted from 9 ``Turtle Scute``
- <c>Kelp Block</c>: crafted from 9 ``Kelp``

## <o>Block Pallette Consistency</o>
### <o>(Vanilla Blocks)</o>
- <ins>Crimson Boat</ins>: crafted from 5 ``Crimson Plank``
    - <ins>Warped Boat</ins>: crafted from 5 ``Warped Plank``
    - <ins>Crimson Boat with Chest</ins>: crafted from 5 ``Crimson Plank`` and 1 ``Chest``
    - <ins>Warped Boat with Chest</ins>: crafted from 5 ``Warped Plank`` and 1 ``Chest``
- <ins>Netherite Horse Armour</ins>: smithed from 1 ``Diamond Horse Armour`` and 1 ``Netherite Ingot``
- <ins>Crimson Wart Carpet</ins>: crafted from 2 ``Nether Wart Block``
    - <ins>Warped Wart Carpet</ins>: crafted from 2 ``Warped Wart Block``
- <ins>Stone Wall</ins>: crafted/stonecut from ``Stone``
- <ins>Deepslate Slab</ins>, <ins>Deepslate Stair</ins>, <ins>Deepslate Wall</ins>, <ins>Deepslate Button</ins>, <ins>Deepslate Pressure Plate</ins>: crafted/stonecut from ``Deepslate``
- <ins>Basalt Slab</ins>, <ins>Basalt Stair</ins>, <ins>Basalt Wall</ins>: crafted/stonecut from ``Basalt``
- <ins>Polished Basalt Slab</ins>, <ins>Polished Basalt Wall</ins>: crafted/stonecut from ``Polished Basalt``
- <ins>Polished Andesite Wall</ins>: crafted/stonecut from ``Polished Andesite``
- <ins>Polished Diorite Wall</ins>: crafted/stonecut from ``Polished Diorite``
- <ins>Polished Granite Wall</ins>: crafted/stonecut from ``Polished Granite``
- <ins>Smoothstone Stair</ins>, <ins>Smoothstone Wall</ins>: crafted/stonecut from ``Smoothstone``
- <ins>Smooth Sandstone Wall</ins>: crafted/stonecut from ``Smooth Sandstone``
- <ins>Smooth Red Sandstone Wall</ins>: crafted/stonecut from ``Smooth Red Sandstone``
- <ins>Cut Sandstone Stair</ins>, <ins>Cut Sandstone Wall</ins>: crafted/stonecut from ``Cut Sandstone``
- <ins>Cut Red Sandstone Stair</ins>, <ins>Cut Red Sandstone Wall</ins>: crafted/stonecut from ``Cut Red Sandstone``
- <ins>Dripstone Slab</ins>, <ins>Dripstone Stair</ins>, <ins>Dripstone Wall</ins>: crafted/stonecut from ``Dripstone``
- <ins>Calcite Slab</ins>, <ins>Calcite Stair</ins>, <ins>Calcite Wall</ins>: crafted/stonecut from ``Calcite``
- <ins>Quartz Bricks Slab</ins>, <ins>Quartz Bricks Stair</ins>, <ins>Quartz Bricks Wall</ins>: crafted/stonecut from ``Quartz Bricks``
- <ins>Smooth Quartz Wall</ins>: crafted/stonecut from ``Smooth Quartz``
- <ins>Smooth Basalt Slab</ins>, <ins>Smooth Basalt Stair</ins>, <ins>Smooth Basalt Wall</ins>: crafted/stonecut from ``Smooth Basalt``
- <ins>Prismarine Bricks Wall</ins>: crafted/stonecut from ``Prismarine Bricks``
- <ins>Dark Prismarine Wall</ins>: crafted/stonecut from ``Dark Prismarine``
- <ins>Purpur Pillar Slab</ins>, <ins>Purpur Pillar Wall</ins>: crafted/stonecut from ``Purpur Pillar``
- <ins>Endstone Slab</ins>, <ins>Endstone Stair</ins>, <ins>Endstone Wall</ins>: crafted/stonecut from ``Endstone``

### <o>(New Blocks)</o>
- <c>Glazed Terracotta</c>: smelted/blasted from Plain ``Terracotta``
- <c>Concrete Powder</c>: crafted from 1 ``Sand/Red Sand`` and 1 ``Gravel``
    - <c>Concrete</c>: converted from <ins>Concrete Powder</ins> contacting _Water_
- <c>Dirty Wool</c>: obtained from killing/shearing Sheep (can be crafted into <ins>Dirty Wool Carpet</ins>, <ins>Dirty Wool Banner</ins>, <ins>Dirty Wool Bed</ins>)
- <c>Bucket of Quicksand</c>: obtained from using ``Water Bottle`` on ``Sand``, generates in Desert Pits, does not obey gravity
    - <c>Bucket of Red Quicksand</c>: obtained from using ``Water Bottle`` on ``Red Sand``, generates in Mesa Pits, does not obey gravity
- <c>Snow Bricks</c>: crafted from 4 ``Snow Block`` (can be crafted/stonecut into <ins>Snow Brick Slab</ins>, <ins>Snow Brick Stairs</ins>, <ins>Snow Brick Wall</ins>)
    - <c>Chiseled Snow</c>: crafted from 2 <ins>Snow Brick Slab</ins> 
- <c>Soulstone</c>: crafted from 4 ``Soul Sand``/``Soul Soil`` (can be crafted/stonecut into <ins>Soulstone Slab</ins>, <ins>Soulstone Stairs</ins>, <ins>Soulstone Wall</ins>)
    - <c>Cut Soulstone</c>: crafted from 4 <ins>Soulstone</ins> (can be crafted/stonecut into <ins>Cut Soulstone Slab</ins>, <ins>Cut Soulstone Stairs</ins>, <ins>Cut Soulstone Wall</ins>)
    - <c>Smooth Soulstone</c>: smelted/blasted from <ins>Soulstone</ins> (can be crafted/stonecut into <ins>Smooth Soulstone Slab</ins>, <ins>Smooth Soulstone Stairs</ins>, <ins>Smooth Soulstone Wall</ins>)
    - <c>Chiseled Soulstone</c>: crafted from 2 <ins>Soulstone Slab</ins>
- <c>Iron Grate</c>: crafted from 8 ``Iron Ingot``
- <c>Golden Grate</c>: crafted from 8 ``Gold Ingot``
    - <c>Golden Railing</c>, <c>Golden Door</c>, <c>Golden Trapdoor</c>: crafted from 6 ``Gold Ingot``
- <c>Copper Railing</c>: crafted from 6 ``Copper Ingot`` (can be aged into <ins>Exposed</ins>/<ins>Weathered</ins>/<ins>Oxidized Copper Railing</ins> or <ins>Waxed Copper Railing</ins>)
- <c>Gilded Blackstone Bricks</c>: crafted from 4 ``Gilded Blackstone`` (can be crafted/stonecut into <ins>Gilded Blackstone Brick Slab</ins>, <ins>Gilded Blackstone Brick Stairs</ins>, <ins>Gilded Blackstone Brick Wall</ins>)
    - <c>Chiseled Gilded Blackstone</c>: crafted from 2 <ins>Gilded Blackstone Brick Slab</ins>
    - <c>Cracked Gilded Blackstone Bricks</c>: smelted/blasted from <ins>Gilded Blackstone Bricks</ins>
- <c>Magma Bricks</c>: crafted from 4 ``Magma Block`` (can be crafted/stonecut into <ins>Magma Brick Slab</ins>, <ins>Magma Brick Stairs</ins>, <ins>Magma Brick Wall</ins>)
    - <c>Chiseled Magma Bricks</c>: crafted from 2 <ins>Magma Brick Slab</ins>
    - <c>Cracked Magma Bricks</c>: smelted/blasted from <ins>Magma Bricks</ins>
- <c>Chiselled Endstone Bricks</c>: crafted from 2 ``Endstone Brick Slab``
    - <c>Cracked Endstone Bricks</c>: smelted/blasted from ``Endstone Bricks``
- <c>Chiselled Red Nether Bricks</c>: crafted from 2 ``Red Nether Brick Slab``
    - <c>Cracked Red Nether Bricks</c>: smelted/blasted from ``Red Nether Bricks``
- <c>Chiselled Clay Bricks</c>: crafted from 2 ``Clay Brick Slab``
    - <c>Cracked Clay Bricks</c>: smelted/blasted from ``Clay Bricks``
- <c>Chiselled Mud Bricks</c>: crafted from 2 ``Mud Brick Slab``
    - <c>Cracked Mud Bricks</c>: smelted/blasted from ``Mud Bricks``

## <o>Miscellaneous</o>
### <o>(Vanilla Interactions)</o>
- using ``Water Bottle`` on ``Concrete Powder`` converts it into ``Concrete``
- using ``Water Bottle`` on ``Grass Block`` converts it into ``Mud``
- using ``Glowstone Dust`` on ``Sign/Hanging Sign`` makes text glow
- using ``Bone Meal`` on small flowers (``Allium``, ``Azure Bluet``, ``Blue Orchid``, ``Cornflower``, ``Dandelion``, ``Closed Eyeblossom``, ``Open Eyeblossom``, ``Lily of the Valley``, ``Oxeye Daisy``, ``Poppy``, ``Orange Tulip``, ``Pink Tulip``, ``Red Tulip``, ``White Tulip``, ``Wither Rose``) spreads them across ``Sand/Grass/Mud/Moss`` (Bedrock Edition parity)
- using ``Bone Meal`` on ``Spore Blossom`` multiplies them under any block except _Leaves_
- harvesting ``Pitcher Plant`` yields ``Pitcher Pod`` along with ``Pitcher Plant``
- harvesting ``Torchflower`` yields ``Torchflower Seed`` along with ``Torchflower``
- ``Sponge`` absorbs ``Ice``, ``Snow Block``, ``Snow Carpets`` and ``Powdered Snow``

### <o>(New Blocks)</o>
- <c>Frame</c>: crafted from 8 ``Stick``, can be used while planning/mapping builds (using any _Block_ on an <ins>Empty Frame</ins> fills it, using any Block on a <ins>Full Frame</ins> swaps out that _Block_)
- (``Composter`` produces <c>Compost</c> instead of ``Bone Meal``, which can be used to grow crops/saplings; new source for renewable ``Dirt``, tilling <ins>Compost</ins> converts it to ``Farmland``)

## <o>Workbench</o>
### <o>Sawmill</o>
- <c>Sawmill</c>: crafted from 1 ``Iron Ingot`` and 3 _Wooden Planks_ (_Logs_ and _Wooden Planks_ can be cut into _Wooden Products_)
- <c>Woodchipper</c>: crafted from 7 _Wooden Slab_ and 1 ``Iron Ingot`` or from 1 ``Composter`` and 1 ``Iron Ingot`` (using _Wooden Tools_, _Wooden Planks_ and miscellaneous _Wooden Items_ on it produces one layer of <ins>Sawdust</ins>; upon reaching 8 layers, it produces <ins>Wood Pulp</ins>)
- <c>Wood Pulp</c>: crafted from 9 <ins>Sawdust</ins>
- <c>Sawdust</c>: crafted from <ins>Wood Pulp</ins> or ``Bamboo``
- <c>Pykrete</c>: crafted from 1 ``Ice`` and 1 <ins>Sawdust</ins> (blast/ghast resistant)
- (<ins>Sawdust</ins>, <ins>Wood Pulp</ins> can be used as fuel in ``Furnace``)
- (``Packed Mud`` can be crafted from 1 ``Mud`` and 1 <ins>Sawdust</ins>)
- (``Paper`` can be crafted from 3 <ins>Sawdust</ins> and 1 ``Water Bottle``)

 <table>
  <tr>
    <th>50% * 1</th>
    <th>75% * 1</th>
    <th>100% * 1</th>
    <th>50% * 2</th>
    <th>75% * 2</th>
    <th>100% * 2</th>
    <th>50% * 3</th>
    <th>75% * 3</th>
    <th>100% * 8</th>
  </tr>
  <tr>
    <th>Stick</th>
    <th>Hanging Sign</th>
    <th>Wooden Axe</th>
    <th>Slab</th>
    <th>Stair</th>
    <th>Wooden Planks</th>
    <th><nano>-</nano></th>
    <th><nano>+</nano></th>
    <th>Wood</th>
  </tr>
  <tr>
    <td>Deadbush</td>
    <td>Sign</td>
    <td>Wooden Pickaxe</td>
    <td>Door</td>
    <td>Fence</td>
    <td>Bamboo Mosaic</td>
    <td></td>
    <td></td>
    <td>Hyphae</td>
  </tr>
  <tr>
    <td>Sapling</td>
    <td>Ladder</td>
    <td>Wooden Shovel</td>
    <td>Trapdoor</td>
    <td>Fence Gate</td>
    <td>Boat</td>
    <td></td>
    <td></td>
    <td>Log</td>
  </tr>
  <tr>
    <td>Pressure Plate</td>
    <td></td>
    <td>Wooden Sword</td>
    <td></td>
    <td></td>
    <td>Boat with Chest</td>
    <td></td>
    <td></td>
    <td>Stem</td>
  </tr>
  <tr>
    <td>Button</td>
    <td></td>
    <td>Wooden Hoe</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Bamboo Block</td>
  </tr>
</table> 

- ``+`` Chest/Barrel/Chiselled Bookshelf/Composter/Jukebox/Noteblock/Bookshelf/Beehive
- ``-`` Cartography Table/Loom/Fletching Table/Smithing Table/Crafting Table/Lectern/Campfire

### <o>Smelters</o>
- ``Furnace/Blast Furnace/Smoker`` can now yield more than one item (via count argument)
- smelting _Iron/Gold Gear_ outputs certain amount of nuggets determined by amount of ingots required per gear multiplied by base number based on durability percentage*, instead of just a single nugget (see [Amaro's Minecraft Rebuild doc](https://docs.google.com/document/d/1hcjAA0sCdIw9qAKpBs5FCjGDc9U5kW2f/edit?tab=t.0#heading=h.1ksv4uv))

   |Tools     |below 25%|above 25%|above 50%|above 75%|100%     |
   |----------|---------|---------|---------|---------|---------|
   |Axe       |15       |18       |21       |24       |27       |
   |Pickaxe   |15       |18       |21       |24       |27       |
   |Sword     |10       |12       |14       |16       |18       |
   |Shears    |10       |12       |14       |16       |18       |
   |Hoe       |10       |12       |14       |16       |18       |
   |Shovel    |5        |6        |7        |8        |9        |

   |Armour    |below 25%|above 25%|above 50%|above 75%|100%     |
   |----------|---------|---------|---------|---------|---------|
   |Chestplate|40       |48       |56       |64       |64*      |
   |Leggings  |35       |42       |49       |56       |63       |
   |Helmet    |25       |30       |35       |40       |45       |
   |Boots     |20       |24       |28       |32       |36       |

### <r>Brewing Stand</r> 
### <r>Cauldron</r>
### <r>Fletching Table</r>