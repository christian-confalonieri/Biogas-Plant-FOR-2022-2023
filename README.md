<h1>Biogas Plant</h1>

[![License: MIT][license-image]][license]

This project is an optional activity of "Foundations of Operations Research", course of "**Computer Science and Engineering**" held at Politecnico di Milano (2022/2023).

**Professor**: Federico Malucelli

**Final Score**: 4 / 4

<h2>Project specification</h2>

You want to plan the two-year supply of raw materials for a biogas power plant. Such a plant produces energy by burning biogas, which is obtained from the bacterial fermentation of organic wastes. 
Specifically, your plant is powered by corn chopping, a residual of agro-industrial operations that you can purchase from 5 local farms. 
The table below shows the quarterly capacity of each farm for the next two years. Quantities are measured in tons.

Farm|T1|T2|T3|T4|T5|T6|T7|T8
:-|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:
1|700|1500|700|0|0|700|1500|0
2|1350|0|450|0|1350|0|450|0
3|0|1500|1500|0|0|1500|1500|0
4|820|1560|820|0|820|1560|820|0
5|0|680|1080|0|0|680|1080|0

Due to crop rotations and corn harvesting periods, farms are unable to supply material in some quarters. Moreover the types of corn chopping provided are different, each coming with its own unitary purchase price, unitary storage cost and percentage of dry matter. The table below shows a summary of these information.

Farm|Purchase price|Storage cost|Dry matter
:-|:-:|:-:|:-:
1|0.20|0.002|15
2|0.18|0.012|28
3|0.19|0.007|35
4|0.21|0.011|37
5|0.23|0.015|42

Your biogas plant must operate by burning a mixture of corn choppings with a dry matter percentage between 20% and 40%. Under these conditions, the yield is 421.6 kWh of energy per ton of burned material. The energy produced by the plant is sold on the market at a price of 0.28 $/kWh. 

Due to state regulations, all biogas plants can produce a maximum of 1950 MWh of energy per quarter. You are allowed to store corn chopping in a silo, whose total capacity is of 500 tons. 

Plan the supply and inventory of your biogas plant with the goal of maximizing your profits (i.e., revenues minus costs).

## Team
|                         |                         |                         |
|-------------------------|-------------------------|-------------------------|
| [Luca Brembilla][github-link-1]          | [Christian Confalonieri][github-link-2]  | Grecya D'Angiò          |
|                         |                         |                         |

<h2>Copyright and license</h2>

This project is copyright 2022.

Licensed under the **[MIT License][license]**; you may not use this software except in compliance with the License.

[license]: https://github.com/christian-confalonieri/Biogas-Plant-FOR-2022-2023/blob/main/LICENSE
[license-image]: https://img.shields.io/badge/License-MIT-blue.svg
[github-link-1]: https://github.com/LucaBrembilla
[github-link-2]: https://github.com/christian-confalonieri
