<template>
  <div class="wrap">
    <div class="wrap-container">
      <div class="resume-box resume-user-box">
        <p>개인정보</p>
        <div class="resume-user-content">
          <label for="resume-user-img-edit">
            <div class='resume-user-img-box'>
                <i v-if="!profileImg" class="far fa-images"><i class="fas fa-plus"></i></i>
                <input type="file" id="resume-user-img-edit" accept="image/*" @change="setProfileImg">
              <p v-if="!profileImg">프로필 사진을 등록해주세요</p>
              <img v-if='profileImg' class="resume-user-img" :src="profileImg" alt="#">
            </div>
          </label>
          <div class="resume-user-profile">
            <div class="resume-user-name-box resume-user-profile-box">
              <span>이름</span>
              <input type="text" class="resume-user-input">
            </div>
            <div class="resume-user-birth-box resume-user-profile-box">
              <span>생년월일</span>
              <input type="text" class="resume-user-input">
            </div>
            <div class="resume-user-mail-box resume-user-profile-box">
              <span>이메일</span>
              <input type="text" class="resume-user-input">
            </div>
            <div class="resume-user-num-box resume-user-profile-box">
              <span>휴대폰</span>
              <input type="text" class="resume-user-input">
            </div>
          </div>
        </div>
      </div>
      <div class="resume-box resume-school-box">
        <p>학력사항</p>
      </div>
      <div class="resume-box resume-license-box">
        <p>자격사항</p>
      </div>
      <div class="resume-box resume-career-box">
        <p>경력사항</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Resume',
  data() {
    return {
      profileImg: '',
    }
  },
  methods: {
    setProfileImg() {
      const photoFile = document.getElementById("resume-user-img-edit");
      this.profileImg = URL.createObjectURL(photoFile.files[0]);
    },
  }
}
</script>

<style>
.resume-box {
  width: 70%;
  height: 600px;
  background-color: #eff0f5;
  box-shadow: 6px 6px 10px -1px rgba(0,0,0,0.2),
              -6px -6px 10px -1px #ffffff;
  border-radius: 20px;
  margin-top: 40px;
  margin-bottom: 40px;
  padding: 30px 40px;
}

.resume-box > p {
  margin-bottom: 30px;
  font-weight: 900;
  font-size: 30px;
}

.resume-user-box .resume-user-content {
  display: flex;
}

.resume-user-content label {
  width: 30%;
  margin-right: 50px;
}

.resume-user-content .resume-user-img-box {
  width: 100%;
  height: 330px;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  position: relative;
  border-radius: 20px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  align-items: center;
}

.resume-user-img-box input[type="file"] {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.resume-user-img-box .fa-images {
  color: rgba(0,0,0,0.7);
  margin: 0;
  position: absolute;
  top: 40%;
  left: 48%;
  transform: translate(-50%, -50%);
  font-size: 50px;
  transition: .3s;
}

.resume-user-img-box .fa-images .fa-plus {
  color: rgba(0,0,0,0.7);
  margin: 0;
  position: absolute;
  bottom: 0;
  right: -30%;
  font-size: 20px;
  transition: .3s;
}

.resume-user-img-box > p {
  color: rgba(0,0,0,0.6);
  position: absolute;
  top:55%;
  left:50%;
  transform: translate(-50%, -50%);
  font-size: 14px;
  width: 100%;
  text-align: center;
  transition: .3s;
}

.resume-user-img-box > img {
  width: 80%;
  height: 80%;
}

.resume-user-content .resume-user-img-box:hover .fa-images,
.resume-user-content .resume-user-img-box:hover .fa-images .fa-plus,
.resume-user-content .resume-user-img-box:hover > p {
  color: #0088ff;
}

.resume-user-content .resume-user-profile {
  width: 60%;
  display: flex;
  flex-direction: column;
}

.resume-user-profile .resume-user-input {
  width: 68%;
  outline: none;
  background: transparent;
  box-shadow: inset 4px 4px 6px -1px rgba(0,0,0,0.2),
            inset -4px -4px 6px -1px #ffffff;
  border: none;
  border-radius: 20px;
  padding-left: 3%;
}

.resume-user-profile .resume-user-profile-box {
  margin: 20px 0;
}

.resume-user-profile-box > span {
  width: 150px;
  display: inline-block;
  font-size: 20px;
  font-weight: 700;
}

.resume-user-profile-box .resume-user-input {
  height: 40px;
}
</style>