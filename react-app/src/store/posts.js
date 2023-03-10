const defaultState = {}

const LOAD_PROFILE_POSTS = 'posts/LOAD_MY_POSTS';
const LOAD_FEED_POSTS = 'posts/LOAD_FEED_POSTS'
const LOAD_POST = 'posts/LOAD_POST';
const CREATE_POST = 'posts/CREATE_POST'
const EDIT_POST = 'posts/EDIT_POST';
const DELETE_POST = 'posts/DELETE_POST'

const loadProfilePosts = payload => {
    return {
        type: LOAD_PROFILE_POSTS,
        payload
    }
}

export const loadProfilePostsThunk = (userId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/posts`)

    if (res.ok) {
        const data = await res.json()
        dispatch(loadProfilePosts(data))
      }
}

const loadFeedPosts = payload => {
    return {
        type: LOAD_FEED_POSTS,
        payload
    }
}

export const loadFeedPostsThunk = (userId) => async (dispatch) => {
    const res = await fetch(`/api/users/${userId}/feed`)

    if (res.ok) {
        const data = await res.json()
        dispatch(loadFeedPosts(data))
      }
}

const loadPost = payload => {
    return {
        type: LOAD_POST,
        payload
    }
}

export const loadPostThunk = (postId) => async (dispatch) => {
    const res = await fetch(`/api/posts/${postId}`)

    if (res.ok) {
        const data = await res.json()
        dispatch(loadPost(data))
      }
}

const createPost = payload => {
    return {
        type: CREATE_POST,
        payload
    }
}

export const createPostThunk = (formData) => async (dispatch) => {

    const res = await fetch(`/api/posts/create`, {
        method: 'POST',
        headers: {
            "Content-Type": "multipart/form-data",
          },
        // body: JSON.stringify({
        //   media,
        //   caption
        // }),
      });

      if (res.ok) {
        // const newData = await res.json()
        dispatch(createPost(res.data))
    }
}

const editPost = payload => {
    return {
        type: EDIT_POST,
        payload
    }
}

export const editPostThunk = (postId, caption) => async (dispatch) => {

    const res = await fetch(`/api/posts/${postId}/edit`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          caption
        }),
      });

      if (res.ok) {
        const newData = await res.json()
        dispatch(editPost(newData))
    }
}

const deletePost = (postId) => {
    return {
        type: DELETE_POST,
        postId
    }
}

export const deletePostThunk = (postId) => async (dispatch) => {
    const post = await fetch(`/api/posts/${postId}/delete`, {
        method: "DELETE"
    })

    if (post.ok) dispatch(deletePost(postId))
}

export default function reducer(state = defaultState, action) {
    const newState = {...state}

    switch (action.type) {
        case LOAD_PROFILE_POSTS:
            return {...newState, ...action.payload}
        case LOAD_FEED_POSTS:
            return {...newState, ...action.payload}
        case LOAD_POST:
            return {...newState, [action.payload.id] : action.payload}
        case CREATE_POST:
            return {...newState, [action.payload.id] : action.payload}
        case EDIT_POST:
            return {...newState, [action.payload.id] : action.payload}
        case DELETE_POST:
            delete newState[action.postId]
            return newState
        default:
            return state;
    }
}
