'use strict';

const element = React.createElement;

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  alteraState() {
      if (this.state.liked) {
        this.setState({ liked: false })
      } else {
        this.setState({ liked: true })
      }
  }

  render() {
    if (this.state.liked) {
      return element(
        'button',
        { onClick: () => this.alteraState(),
          class: "btn_1 size_md p-t-sm"
        },
        'Un Like'
      );
    }

    return element(
      'button',
      { onClick: () => this.alteraState(),
        class: "btn_2 size_sm p-t-sm"
      },
      'Like'
    );
  }
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(element(LikeButton), domContainer);