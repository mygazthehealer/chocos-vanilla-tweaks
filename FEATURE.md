<style>
r {color: Red}
o {color: Orange}
g {color: Green}
c {color: Cyan}
</style>

<h3>NOTE:</h3>

- Features marked <g>green</g> have been implemented, <o>orange</o> is work-in-progress and <r>red</r> has not yet been implemented.
- Blocks/Items marked <c>cyan</c> are modded and ``nano`` are vanilla.

## Inventory
### <o>Stacking</o>
- ``Horse Armour``, ``Saddle``, ``Minecart``, ``Boat``, Filled Buckets (``Water/Milk/Lava/Powder Snow Bucket``), Potions (``Regular/Splash/Lingering Potions``) now stacks to 16 (instead of 1)
- ``Empty Bucket``, ``Eye of Ender`` now stacks to 16 (instead of 64)
- ``Bed``, ``Cake``, ``Banner Pattern``, ``Disc``, ``Enchanted Book``, ``Water Bottle``, Ingredient Potions (``Awkward/Thick/Mundane Potions``), ``Soup/Stew``, ``Spyglass``, ``Goat Horn`` now stacks to 64 (instead of 1)
- ``Armour Stand``, ``Egg``, ``Snowball``, ``Sign``, ``Hanging Sign``, ``Honey Bottle`` now stacks to 64 (instead of 16)
- ``Splash Potions`` and ``Lingering Potions`` have a cooldown of 2 seconds upon usage

### <o>Storage Blocks</o>
- <c>Blazing Sand</c>: crafted from 9 ``Blaze Powder``, affected by gravity, deals damage on contact similar to ``Magma Block``
- <c>Glowing Sand</c>: crafted from 9 ``Glowstone Dust``, affected by gravity, emits light similar to ``Glowstone``
- <c>Magma Cream Block</c>: crafted from 9 ``Magma Cream``, behaves like ``Slime Block``, directional like ``Log``
- <c>Charcoal Block</c>: crafted from 9 ``Charcoal``, smelts 80 items in Furnace similar to ``Coal Block``
- <c>Gunpowder Block</c>: crafted from 9 ``Gunpowder``, affected by gravity
- <c>Flintstone</c>: crafted from 9 ``Flint``, creates fire on flamable blocks when pushed/pulled besides ``Iron Block``
- <c>Amethyst Shard Block</c>: crafted from 9 ``Amethyst Shard``
- <c>Quartz Crystal Block</c>: crafted from 9 ``Nether Quartz``
- <c>Prismarine Shard Block</c>: crafted from 9 ``Prismarine Shard``
- <c>Prismarine Crystal Block</c>: crafted from 9 ``Prismarine Crystal``, emits light similar to ``Sea Lantern``
- <c>Echo Shard Block</c>: crafted from 9 ``Echo Shard``
- <c>Ender Pearl Block</c>: crafted from 9 ``Ender Pearl``
- <c>Netherite Scrap Heap</c>: crafted from 9 ``Netherite Scrap``
- <c>Sugar Cube</c>: crafted from 9 ``Sugar``, dissolves upon contact with ``Water``, ``Snowball`` and ``Powdered Snow``
- <c>Sugarcane Block</c>: crafted from 9 ``Sugarcane``, has a chance to produce more Sugarcane Block when placed on ``Sand/Grass/Mud`` besides ``Water``, directional like ``Log``
- (``Bamboo Block`` has a chance to produce more ``Bamboo Block`` when placed on ``Sand/Grass/Mud/Moss``)
- (Crop Crates: new storage blocks for crops, directional like ``Log``)
    - <c>Apple Crate</c>: crafted from 9 ``Apple``
    - <c>Carrot Crate</c>: crafted from 9 ``Carrot``
    - <c>Beetroot Crate</c>: crafted from 9 ``Beetroot``
    - <c>Potato Crate</c>: crafted from 9 ``Potato``
    - <c>Chorus Fruit Crate</c>: crafted from 9 ``Chorus Fruit``
    - <c>Sweet Berry Crate</c>: crafted from 9 ``Sweet Berry``
    - <c>Glow Berry Crate</c>: crafted from 9 ``Glow Berry``
    - <c>Nether Wart Crate</c>: crafted from 9 ``Nether Wart``
- (Meat Barrels: new storage blocks for meats, directional like ``Log``)
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
- <c>String Spool</c>: crafted from 9 ``String``, directional like ``Log``

## <o>Miscellaneous<o>
- using ``Water Bottle`` on ``Concrete Powder`` converts it into ``Concrete``
- using ``Water Bottle`` on ``Grass Block`` converts it into ``Mud``
- using ``Glowstone Dust`` on ``Sign/Hanging Sign`` makes text glow
- using ``Bone Meal`` on small flowers (``Allium``, ``Azure Bluet``, ``Blue Orchid``, ``Cornflower``, ``Dandelion``, ``Closed Eyeblossom``, ``Open Eyeblossom``, ``Lily of the Valley``, ``Oxeye Daisy``, ``Poppy``, ``Orange Tulip``, ``Pink Tulip``, ``Red Tulip``, ``White Tulip``, ``Wither Rose``) spreads them across ``Sand/Grass/Mud/Moss`` (Bedrock Edition parity)
- using ``Bone Meal`` on ``Spore Blossom`` multiplies them under any block except ``Leaves``
- harvesting ``Pitcher Plant`` yields ``Pitcher Pod`` along with ``Pitcher Plant``
- harvesting ``Torchflower`` yields ``Torchflower Seed`` along with ``Torchflower``
- ``Sponge`` absorbs ``Ice``, ``Snow Block``, ``Snow Carpets`` and ``Powdered Snow``

## Workbench
### <r>Smelters</r>
- ``Furnace/Blast Furnace/Smoker`` can now yield more than one item (via count argument)
- smelting Metal Gear outputs certain amount of nuggets determined by amount of ingots required per gear multiplied by base number based on durability percentage*, instead of just a single nugget (see [Amaro's Minecraft Rebuild doc](https://docs.google.com/document/d/1hcjAA0sCdIw9qAKpBs5FCjGDc9U5kW2f/edit?tab=t.0#heading=h.1ksv4uv))

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