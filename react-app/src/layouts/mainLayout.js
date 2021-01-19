import bgimage from "../public/menu_2.jpg"

function Home(props) {
  return (
    <div>
        <div class="header">
            <div class="float c-c p-a-s">primeiro layout</div>
            <img class="full-width" src={bgimage} alt="main layout" />
        </div>
        {props.children}
    </div>
  );
}

export default Home;
