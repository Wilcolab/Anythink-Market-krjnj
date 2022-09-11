import React from "react";
import agent from "../../agent";
import { connect } from "react-redux";
import { APPLY_TITLE_FILTER } from "../../constants/actionTypes";

const mapStateToProps = (state) => ({
  ...state.itemList,
  title: "",
});

const mapDispatchToProps = (dispatch) => ({
  onChangeTitle: (title, pager, payload) =>
    dispatch({ type: APPLY_TITLE_FILTER, title, pager, payload }),
});

const Search = (props) => {
  // const title = props.title;
  const changeHandler = (ev) => {
    ev.preventDefault();
    const query = ev.target.value.trim();
    if (query.length > 2) {
      console.log(query);
      props.onChangeTitle(
        query,
        (page) => agent.Items.byTitle(query, page),
        agent.Items.byTitle(query)
      );
    } else if (query.length === 0) {
      props.onChangeTitle("", agent.Items.all, agent.Items.all());
    }
  };
  return (
    <div class="mx-2">
      <input
        id="search-box"
        type="text"
        class="form-control"
        onChange={changeHandler}
        placeholder="What is that you truly desire?"
      />
    </div>
  );
};

export default connect(mapStateToProps, mapDispatchToProps)(Search);
