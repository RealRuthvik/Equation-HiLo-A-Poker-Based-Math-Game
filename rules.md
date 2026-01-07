# **Equation Hi-Lo: Game Documentation**

This guide provides the core mechanics, rules, and logic required to build a digital version of the **Equation Hi-Lo** game, inspired by the Netflix survival show *The Devil's Plan*.

## **1\. Core Mechanics**

The game is a hybrid of Poker-style betting, High-Low prediction, and the math puzzle "24."

### **Players**

* **2 Active Players:** Competitors who bet chips and construct equations.  
* **1 Dealer (System):** Manages the deck, handles payouts, and validates mathematical strings.

### **The Deck**

* **Number Cards:** Values 0–10.  
* **Suits (Tie-breakers):** Gold \> Silver \> Bronze \> Dirt.  
* **Standard Operations:** Every player starts with permanent access to \+, \-, and ÷.  
* **Special Operations:** × (Multiplication) and √ (Square Root) are hidden within the number deck.

## **2\. Gameplay Loop**

### **Phase 1: Ante & The Hidden Card**

1. Both players pay a **1 Chip Ante**.  
2. Each player is dealt **1 Private Card** (visible only to them).  
3. **Betting Round 1:** Standard Poker actions (Check, Bet, Call, or Fold).

### **Phase 2: The Public Reveal**

1. Each player is dealt **3 Face-up Cards**.  
2. **Special Card Rule:** If a player receives a × or √ from the deck, they keep it but must "discard" one of their basic operations.  
3. The Dealer then provides an extra number card to ensure every player always has exactly **4 numbers**.  
4. **Final Betting Round:** Stakes are raised based on the visible cards of the opponent.

### **Phase 3: The Declaration**

Players secretly choose one of three targets:

* **LOW:** Aiming for a result closest to **1**.  
* **HIGH:** Aiming for a result closest to **20**.  
* **SWING:** A high-risk bet. You must win **BOTH** High and Low targets. If you lose either, you lose the entire pot.

## **3\. Mathematical Rules (The "Engine")**

When implementing the Python logic, the following constraints must be hard-coded:

* **PEMDAS/BODMAS:** Multiplication, Division, and Square Roots take priority over Addition and Subtraction.  
* **No Brackets:** Players cannot use parentheses to alter the calculation order.  
* **Mandatory Usage:** Every equation must use all **4 number cards** and **3 operation cards**.  
* **Target Logic:** Results can be negative or decimals. (Example: 0.8 is numerically closer to 1 than 1.5 is).  
* **Comparison:** If two players both target "High," the one numerically closest to 20 wins.

## **4\. Winning and Payouts**

| Scenario | Outcome |
| :---- | :---- |
| **Split Pot** | Player A chooses High and Player B chooses Low; both win their respective halves. |
| **Winner-Takes-All** | Both players choose the same target; the closer result wins the full pot. |
| **Swing Success** | If a player chooses Swing and has the best High AND best Low hand, they take the pot. |
| **Swing Failure** | If a Swing player loses either the High or Low comparison, the opponent wins the pot. |

### **Tie-Breakers**

If the numerical results are identical, the winner is determined by the **Suit Rank** of the highest-ranking color card among the four numbers used in the equation.

## **5\. Implementation Strategy (Python Build)**

For a robust build, consider using the itertools.permutations library. This allows you to create a **Solver Function** that:

1. Generates all permutations of the 4 numbers.  
2. Generates all permutations of the 3 available operations.  
3. Evaluates the resulting strings using eval() (with proper security handling) to find the optimal result for the player's chosen target.