import { Children } from "react"
import bgimage from "../public/menu_2.jpg"

function Home(props) {
  return (
    <div>
        <div class="header">
            <div class="float c-c p-a-s">primeira tela</div>
            <img class="full-width" src={bgimage} />
        </div>
        {props.children}
    </div>
  );
}

export default Home;
