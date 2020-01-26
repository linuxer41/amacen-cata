import Link from 'next/link';
import fetch from 'isomorphic-fetch';

const SnipptLink = props => (
  <>
    <Link href="/snippt/[id]" as={`/snippt/${props.id}`}>
      <a>{props.title}</a>
    </Link>
  </>
);

const Index = props => {
  console.log(props.snippt)
  return(
    <>
      <h1>Libros</h1>
      <ul>
        {props.snippt.map(snippt => (
          <li key={snippt.id}>
            <SnipptLink id={snippt.id} title={snippt.title}/>
          </li>
        ))}
      </ul>
    </>
  )
};

Index.getInitialProps = async function() {
  const res = await fetch('http://127.0.0.1:8000/s/snippets/');
  const data = await res.json();

  console.log(`Show data fetched. Count: ${data.length}`);

  return {
    snippt: data
  };
};

export default Index;