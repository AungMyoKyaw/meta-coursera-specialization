import { useFormik } from 'formik';

import './Form.css';

function Form() {
  // be called when the form is submitted
  const formik = useFormik({
    initialValues: {
      dinersize: 0,
      date: '',
      time: '',
      fullname: '',
      contactnumber: '',
      comments: '',
    },
    onSubmit: (values) => {
      alert("Your reservation has been submitted!");
      formik.resetForm();
    },
  });
  return (
    <div className="formSection">
      <form className="form" onSubmit={formik.handleSubmit}>
        <label htmlFor="dinersize">Diner Size</label>
        <input
          id="dinersize"
          name="dinersize"
          type="number"
          onChange={formik.handleChange}
          value={formik.values.dinersize}
        />

        <label htmlFor="date">Date</label>
        <input
          id="date"
          name="date"
          type="date"
          onChange={formik.handleChange}
          value={formik.values.date}
        />

        <label htmlFor="time">Time</label>
        <input
          id="time"
          name="time"
          type="time"
          onChange={formik.handleChange}
          value={formik.values.time}
        />

        <label htmlFor="fullname">Full Name</label>
        <input
          id="fullname"
          name="fullname"
          type="text"
          maxLength="50"
          onChange={formik.handleChange}
          value={formik.values.fullname}
        />

        <label htmlFor="contactnumber">Contact Number</label>
        <input
          id="contactnumber"
          name="contactnumber"
          type="tel"
          onChange={formik.handleChange}
          value={formik.values.contactnumber}
        />

        <label htmlFor="comments">Comments</label>
        <textarea
          id="comments"
          name="comments"
          type="text"
          lines="5"
          maxLength="200"
          onChange={formik.handleChange}
          value={formik.values.comments}
        />

        <button type="submit">Reserve Table</button>
      </form>
    </div>
  );
}

export default Form;
