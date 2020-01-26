import Link from 'next/link';

const linkStyle = {
  marginRight: 15
};

const Header = () => (
  <div className="header">
    <Link href="/">
      <a style={linkStyle}>Principal</a>
    </Link>
    <Link href="/about">
      <a style={linkStyle}>About</a>
    </Link>
    <style jsx>
      {`
      .header {
        border-bottom: 1px solid #DDD;
      }
      
      `}
    </style>
  </div>
);

export default Header;