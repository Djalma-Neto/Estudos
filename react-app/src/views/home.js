import MainLayout from '../layouts/mainLayout'

function Home() {
  return (
    <MainLayout>
      <form  method="GET" action="/teste">
        conteudo
        <button type="submit">click</button>
      </form>
    </MainLayout>
  );
}

export default Home;
