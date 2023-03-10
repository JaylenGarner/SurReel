import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { createRoomThunk } from '../../../../store/rooms';
import { loadRoomsThunk } from '../../../../store/rooms';
import './CreateRoomForm.css'

const CreateRoomForm = () => {
    const history = useHistory();
    const dispatch = useDispatch();
    const user = useSelector((state) => state.session.user)
    const [users, setUsers] = useState([]);
    const rooms = useSelector((state) => state.rooms)
    const [selectedUsers, setSelectedUsers] = useState([]);
    const [error, setError] = useState();

    useEffect(() => {
      async function fetchData() {
        const response = await fetch('/api/users/');
        const responseData = await response.json();
        setUsers(responseData.users);
      }
      fetchData();
    }, [selectedUsers]);

    const toggleSelection = (selectedUser) => {
        let newSelectedUsers = [...selectedUsers]

        // If the user is not selected, add it to the list of selected users
        if (!newSelectedUsers.includes(selectedUser.id)) {
          newSelectedUsers.push(selectedUser.id);
        } else {
          // If the user is already selected, remove it from the list of selected users
          newSelectedUsers.splice(newSelectedUsers.indexOf(selectedUser.id), 1)
        }

        setSelectedUsers(newSelectedUsers);
    };

    const userComponents = users.map((user) => {
        return (
            <div key={user.id} className='user-selection-container'>
            <input
              className='user-selection-input-box'
              type="checkbox"
              onClick={() => toggleSelection(user)}
              />
              <img className='user-selection-image' src={user.image}></img>
              <span className='user-selection-username'>{user.username}</span>
            </div>
        );
      });

    const checkForExistingConversation = () => {
      let doesExist = false
      const selected = [...selectedUsers]
      selected.push(user.id)
      const sortSelected = selected.sort()


      Object.values(rooms).forEach((serv) => {
        let members = serv.members
        let memberIds = members.map((member) => {
          return member.member.id
        }).sort()

        let areArraysEqual = sortSelected.length === memberIds.length && sortSelected.every((value, index) => value === memberIds[index])

        if (areArraysEqual) {
          doesExist = true
          return true
        }
      })

      return doesExist
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        setError()

        if (Object.keys(selectedUsers).length === 0) {
          // show an error message or alert to inform the user that at least one user is required
          setError("Please select at least one user to start a conversation with");
          return;
        }

        const conversationExists = checkForExistingConversation()

        if (conversationExists === true) {
          setError("There is an existing conversation based off of your selection");
          return;
        }
        console.log(selectedUsers, 'Before dispatch')


     const createServ = await dispatch(createRoomThunk(selectedUsers))
     const loadServs = await dispatch(loadRoomsThunk())
     const redirectToProfile = history.push('/messages')

     console.log(createServ)

    };

    return (
        <div>
            <div className='dm-user-selection-header-container'>
                <h1 className='dm-user-selection-header'>Choose one or more users to chat with</h1>
            </div>
            <div className='user-selection-error'>
              {error && <span>{error}</span>}
            </div>
          {userComponents}
          <div className='user-selection-submit-button-container'>
          <button onClick={handleSubmit} className='user-selection-submit-button'>Start Chat</button>
          </div>
        </div>
      );
    }


export default CreateRoomForm;
