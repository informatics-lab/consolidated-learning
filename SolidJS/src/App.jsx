import styles from './App.module.css';

function App() {
  return (
    <div>
      <header>
        <div>Nav</div>
        <nav>
          <ul>
            <li><a href="#ingredients">Ingredients</a></li>
            <li><a href="#steps">Steps</a></li>
            <li><a href="#subsribe">Subscribe</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <h1>Good Old Fashioned Pancakes</h1>
        <img
          src="https://images.unsplash.com/photo-1575853121743-60c24f0a7502?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8cGFuY2FrZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=60"
          alt="pancake"
          width="250"
        />
        <h2 id="ingredients">Ingredients</h2>
        <ol>
          <li><input type="checkbox" /> 1 ½ cups all-purpose flour</li>
          <li><input type="checkbox" /> 3 ½ teaspoons baking powder</li>
          <li><input type="checkbox" /> 1 teaspoon salt</li>
          <li><input type="checkbox" /> 1 tablespoon white sugar</li>
          <li><input type="checkbox" /> 1 ¼ cups milk</li>
          <li><input type="checkbox" /> 1 egg</li>
        </ol>
        <h2 id="steps">Steps</h2>
        <h4>Step 1</h4>
        <p>
          In a large bowl, sift together the flour, baking powder, salt and sugar.
          Make a well in the center and pour in the milk, egg and melted butter;
          mix until smooth.
        </p>
        <h4>Step 2</h4>
        <p>
          Heat a lightly oiled griddle or frying pan over medium-high heat. Pour
          or scoop the batter onto the griddle, using approximately 1/4 cup for
          each pancake. Brown on both sides and serve hot.
        </p>
      </main>
      <hr />
      <footer>
        <h6 id="subscribe">Subscribe</h6>
        <form onsubmit="alert('Subscribed')">
          <input type="text" placeholder="Enter Email Address" />
          <button>Submit</button>
        </form>
        <br />
        <div>&copy; dakota kelly at Allrecipe.com</div>
      </footer>
    </div>
  );
}

export default App;
